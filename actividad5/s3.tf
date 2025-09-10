resource "random_id" "bucket_suffix" {
  byte_length = 7
}

resource "aws_s3_bucket" "carlos_bucket" {
  bucket = "carlos-bucket-${random_id.bucket_suffix.hex}" 
}

output "bucket_name" {
  value = aws_s3_bucket.carlos_bucket.bucket
}