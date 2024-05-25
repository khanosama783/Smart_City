resource "aws_s3_bucket" "s3-4-data-engineering-2" {
  bucket = "s3-4-data-engineering-2"
  tags = {
    Name = "data-engineering-2-s3"
    Environment = "Dev"
  }
}