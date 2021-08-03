resource "aws_api_gateway_model" "nys_ei_model" {
  rest_api_id  = aws_api_gateway_rest_api.nys_ei.id
  name         = "childdetails"
  description  = "a JSON schema for intake form"
  content_type = "application/json"
  schema       = file("${path.module}/model.json")
}

