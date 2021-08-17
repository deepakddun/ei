resource "aws_iam_role_policy_attachment" "role_policy_attachment" {
  policy_arn = aws_iam_policy.aws_ei_sts_policy.arn
  role = aws_iam_role.aws_ei_sts_role.name
}