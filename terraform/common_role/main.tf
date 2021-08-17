provider "aws" {
  region = "us-east-2"
}

terraform {
  required_version = " > 0.14"
  required_providers {
    aws = "~> 3.0"
  }
  backend "s3" {
    bucket = "nyeisterraformstatedata2"
    key    = "nys-ei-app/api-gateway/aws_sts_role.tfstate"
    region = "us-east-2"

    dynamodb_table = "terraform-up-and-running-locks-2"
    encrypt        = true

  }
}