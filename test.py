from lambda_function import lambda_handler

response = lambda_handler({}, {})

assert response["statusCode"] == 200
print("Test Passed")
