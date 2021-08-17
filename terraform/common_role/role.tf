resource "aws_iam_role" "aws_ei_sts_role" {
  name = "aws_ei_sts_role"

  # Terraform's "jsonencode" function converts a
  # Terraform expression result to valid JSON syntax.
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
       Effect: "Allow",
            Principal: {
                "Service":"states.amazonaws.com"
            },
            Action: "sts:AssumeRole"
      },
    ]
  })

  tags = {
    role = "STS-ROLE",
    Purpose="Will be used by Step functions"
  }
}