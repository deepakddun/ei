provider "aws" {
  region = "us-east-2"
}

terraform {
  backend "s3" {
    bucket = "nyeisterraformstatedata2"
    key    = "nys-ei-app/lambda/aws_lambda_sendemail_role.tfstate"
    region = "us-east-2"

    dynamodb_table = "terraform-up-and-running-locks-2"
    encrypt        = true
  }
}