resource "aws_iam_policy" "aws_ei_sts_policy" {
  name = "aws_ei_sts_policy"

  # Terraform's "jsonencode" function converts a
  # Terraform expression result to valid JSON syntax.
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect: "Allow",
        Action: "lambda:InvokeFunction",
        Resource: "arn:aws:lambda:*:427128480243:function:*"
      },
      {

        Effect: "Allow",
        Action: "sns:Publish",
        Resource: "*"
      },
      {
        Effect: "Allow",
        Action: [
          "execute-api:Invoke",
          "execute-api:ManageConnections"
        ],
        Resource: "arn:aws:execute-api:us-east-2:427128480243:*"
      }
    ]
  })

}