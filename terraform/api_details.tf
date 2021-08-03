resource "aws_api_gateway_request_validator" "nys_ei_request_validator" {
  name                        = "nys_ei_request_validator"
  rest_api_id                 = aws_api_gateway_rest_api.nys_ei.id
  validate_request_body       = true
  validate_request_parameters = false
}

resource "aws_api_gateway_method" "nys_ei_post_method" {
  rest_api_id   = aws_api_gateway_rest_api.nys_ei.id
  resource_id   = aws_api_gateway_resource.nys_ei_resource.id
  http_method   = "POST"
  authorization = "NONE"
  request_models = aws_api_gateway_model.nys_ei_model.name
  request_validator_id = aws_api_gateway_request_validator.nys_ei_request_validator.id

}

