variable "region" {
  type    = string
  default = "us-east-2"
}

variable "function_name" {
  type = string
  default = "test_ei_fucnction"
}

data "aws_iam_account_alias" "current" {}