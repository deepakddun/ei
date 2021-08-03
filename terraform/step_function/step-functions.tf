provider "aws" {
  region="us-east-2"

}

terraform {
  required_version = "> 0.12.0"
  required_providers {
    aws = "~> 3.0"
  }
  backend "s3" {
    bucket = "nyeisterraformstatedata2"
    key    = "nys-ei-app/step-functions/terraform_step_functions.tfstate"
    region = "us-east-2"
    dynamodb_table = "terraform-up-and-running-locks-2"
    encrypt        = true
  }
}

resource "aws_sfn_state_machine" "nys_ei_workflow" {
  name = "nys-ei-worflow"
  role_arn = data.aws_iam_role.step_function_role.arn
  definition = file("${path.module}/state.json")
  type = "STANDARD"
  logging_configuration {
    log_destination        = "arn:aws:logs:us-east-2:427128480243:log-group:nys-ei-app/step-function:*"
    include_execution_data = true
    level                  = "ALL"
  }


}