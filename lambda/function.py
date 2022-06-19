""" Function checks scan result of ECR image. """
import logging
import boto3
from botocore.exceptions import ClientError

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

client = boto3.client("ecr")


def get_image_info(repo, digest):
    """Get additional info about the image."""
    try:
        image_info_list = client.batch_get_image(
            repositoryName=repo,
            imageIds=[
                {"imageDigest": digest},
            ],
        )
    except ClientError as error:
        logging.error("Unexpected error")
        raise error

    image_info = image_info_list["images"][0]

    return image_info


def add_image_tag(repo, manifest, digest):
    """Add 'vulnerable' tag prefix to image."""
    try:
        response = client.put_image(
            repositoryName=repo,
            imageManifest=manifest,
            imageTag="vulnerable-" + digest[7:],
            imageDigest=digest,
        )
    except ClientError as error:
        logging.error("Unexpected error")
        raise error

    LOGGER.info("Image tag 'vulnerable' added!")
    return response


def lambda_handler(event, _):
    """Lambda handler."""

    image = event["resources"][0]
    image_tags = event["detail"]["image-tags"]
    image_digest = event["detail"]["image-digest"]
    image_repository = event["detail"]["repository-name"]

    LOGGER.info(f"Image: {image} with tag(s) {image_tags} contains vulnerabilities.")

    image_info = get_image_info(image_repository, image_digest)
    response = add_image_tag(
        image_repository, image_info["imageManifest"], image_digest
    )

    return {
        "statusCode": response["ResponseMetadata"]["HTTPStatusCode"],
    }
