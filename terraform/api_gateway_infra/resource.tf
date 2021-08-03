resource "aws_api_gateway_resource" "nys_ei_resource" {
  rest_api_id = aws_api_gateway_rest_api.nys_ei.id
  parent_id   = aws_api_gateway_rest_api.nys_ei.root_resource_id
  path_part   = "add"
  depends_on  = [aws_api_gateway_rest_api.nys_ei]
}