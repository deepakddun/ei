data "archive_file" "zip_file" {
  type        = "zip"
  source_dir  = "${path.module}/code"
  output_path = "${path.module}/code.zip"
}



resource "aws_lambda_function" "aws_ei_lambda_send_confirmation_email" {
  filename         = "code.zip"
  function_name    = "send_email"
  role             = aws_iam_role.aws_ei_lambda_ses_role.arn
  handler          = "send_email.send"
  source_code_hash = filebase64sha256(data.archive_file.zip_file.output_path)
  runtime          = "python3.8"
  depends_on       = [aws_iam_role.aws_ei_lambda_ses_role,data.archive_file.zip_file]
}

output "lambda_arn" {
  value = aws_lambda_function.aws_ei_lambda_send_confirmation_email.arn
}