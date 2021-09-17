provider "aws" {
  region = "us-east-2"

}

terraform {
  required_version = "> 0.12.0"
  required_providers {
    aws = "~> 3.0"
  }

  backend "s3" {
    bucket = "nyeisterraformstatedata2"
    key    = "nys-ei-app/api-gateway/terraform_api_gateway.tfstate"
    region = "us-east-2"

    dynamodb_table = "terraform-up-and-running-locks-2"
    encrypt        = true
  }
}

resource "aws_api_gateway_rest_api" "nys_ei" {
  name = "nys_ei"
  endpoint_configuration {
    types = ["REGIONAL"]
  }
}

