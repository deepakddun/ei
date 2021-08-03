provider "aws"{
  region = "us-east-2"

}

terraform {
  required_version = "> 0.12.0"
  required_providers {
    aws = "~> 3.0"
  }
}

resource "aws_api_gateway_rest_api" "nys_ei" {
  name = "nys_ei"
  endpoint_configuration {
    types = ["REGIONAL"]
  }
}