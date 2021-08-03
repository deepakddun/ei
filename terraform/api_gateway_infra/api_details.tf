resource "aws_api_gateway_request_validator" "nys_ei_request_validator" {
  name                        = "nys_ei_request_validator"
  rest_api_id                 = aws_api_gateway_rest_api.nys_ei.id
  validate_request_body       = true
  validate_request_parameters = false
}

resource "aws_api_gateway_method" "nys_ei_post_method" {
  rest_api_id          = aws_api_gateway_rest_api.nys_ei.id
  resource_id          = aws_api_gateway_resource.nys_ei_resource.id
  http_method          = "POST"
  authorization        = "NONE"
  request_models       = {
    "application/json" = aws_api_gateway_model.nys_ei_model.name
  }
  request_validator_id = aws_api_gateway_request_validator.nys_ei_request_validator.id
}

resource "aws_api_gateway_integration" "nys_ei_integration" {
  http_method             = aws_api_gateway_method.nys_ei_post_method.http_method
  resource_id             = aws_api_gateway_resource.nys_ei_resource.id
  rest_api_id             = aws_api_gateway_rest_api.nys_ei.id
  integration_http_method = "POST"
  type                    = "AWS"
  uri                     = "arn:aws:apigateway:${var.region}:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-2:427128480243:function:test_ei_fucnction:DEV/invocations"
}


resource "aws_api_gateway_integration_response" "nys_ei__integration_response" {
  http_method = "POST"
  resource_id = aws_api_gateway_resource.nys_ei_resource.id
  rest_api_id = aws_api_gateway_rest_api.nys_ei.id
  status_code = 200
  /*response_templates = {
    "application/json" = jsonencode({

      "message_str" : "report requested, check your phone shortly"

    })
  }*/

  response_parameters = {
    "method.response.header.Access-Control-Allow-Headers" : "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
    "method.response.header.Access-Control-Allow-Methods" : "'POST'",
    "method.response.header.Access-Control-Allow-Origin" : "'*'",
  }
  depends_on = [aws_api_gateway_integration.nys_ei_integration, aws_api_gateway_method_response.nys_ei_method_response]
}

resource "aws_api_gateway_method_response" "nys_ei_method_response" {
  http_method = "POST"
  resource_id = aws_api_gateway_resource.nys_ei_resource.id
  rest_api_id = aws_api_gateway_rest_api.nys_ei.id
  status_code = 200
  response_parameters = {
    "method.response.header.Access-Control-Allow-Headers" : false,
    "method.response.header.Access-Control-Allow-Origin" : false,
    "method.response.header.Access-Control-Allow-Methods" : false
  }
  depends_on = [aws_api_gateway_method.nys_ei_post_method, aws_api_gateway_integration.nys_ei_integration]
}


// options method
resource "aws_api_gateway_method" "nys_ei_options_method" {
  http_method   = "OPTIONS"
  resource_id   = aws_api_gateway_resource.nys_ei_resource.id
  rest_api_id   = aws_api_gateway_rest_api.nys_ei.id
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "nys_ei_options_integration" {
  http_method = aws_api_gateway_method.nys_ei_options_method.http_method
  resource_id = aws_api_gateway_resource.nys_ei_resource.id
  rest_api_id = aws_api_gateway_rest_api.nys_ei.id
  type        = "MOCK"
  request_templates = {
    "application/json" = jsonencode({
      statusCode = 200
    })
  }
}

resource "aws_api_gateway_method_response" "nys_ei_method_options_response" {
  http_method = "OPTIONS"
  resource_id = aws_api_gateway_resource.nys_ei_resource.id
  rest_api_id = aws_api_gateway_rest_api.nys_ei.id
  status_code = 200
  response_parameters = {
    "method.response.header.Access-Control-Allow-Headers" : true,
    "method.response.header.Access-Control-Allow-Origin" : true,
    "method.response.header.Access-Control-Allow-Methods" : true,
    "method.response.header.Access-Control-Allow-Credentials" : true
  }
  response_models = {
    "application/json" = "Empty"
  }

  depends_on = [aws_api_gateway_method.nys_ei_options_method, aws_api_gateway_integration.nys_ei_options_integration]
}

resource "aws_api_gateway_integration_response" "create_report_integration_options_response" {
  http_method = "OPTIONS"
  resource_id = aws_api_gateway_resource.nys_ei_resource.id
  rest_api_id = aws_api_gateway_rest_api.nys_ei.id
  status_code = 200
  response_templates = {

  }
  response_parameters = {
    "method.response.header.Access-Control-Allow-Headers" : "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
    "method.response.header.Access-Control-Allow-Methods" : "'POST,OPTIONS'",
    "method.response.header.Access-Control-Allow-Origin" : "'*'",
    "method.response.header.Access-Control-Allow-Credentials" : "'true'"
  }
  depends_on = [aws_api_gateway_method.nys_ei_options_method, aws_api_gateway_integration.nys_ei_options_integration
  , aws_api_gateway_method_response.nys_ei_method_options_response]
}

data "aws_lambda_function" "existing_lambda_function" {
  function_name = var.function_name
}

data "aws_caller_identity" "current" {}

data "aws_lambda_alias" "DEV" {
  function_name = data.aws_lambda_function.existing_lambda_function.function_name
  name          = "DEV"
}

# Lambda permission
resource "aws_lambda_permission" "apigw_lambda_nys_ei" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = data.aws_lambda_function.existing_lambda_function.function_name
  principal     = "apigateway.amazonaws.com"

  # More: http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-control-access-using-iam-policies-to-invoke-api.html
  source_arn = "arn:aws:execute-api:${var.region}:${data.aws_caller_identity.current.id}:${aws_api_gateway_rest_api.nys_ei.id}/*/${aws_api_gateway_method.nys_ei_post_method.http_method}${aws_api_gateway_resource.nys_ei_resource.path}"
  qualifier     = data.aws_lambda_alias.DEV.name
}