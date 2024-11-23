import os
import subprocess
import sys

# List of GF patterns
patterns = [
    "api-keys",
    "asymmetric-keys_secrets",
    "auth",
    "aws-keys",
    "aws-keys_secrets",
    "aws-mws-key",
    "aws-s3_secrets",
    "aws-secret-key",
    "google-keys_secrets",
    "google-oauth_secrets",
    "google-service-account_secrets",
    "google-token_secrets",
    "heroku-keys_secrets",
    "github_secrets",
    "facebook-access-token",
    "slack-token",
    "slack-token_secrets",
    "slack-webhook_secrets",
    "s3-buckets",
    "sec",
    "secrets",
    "paypal-token_secrets",
    "php-callbacks",
    "php-informationdisclosure",
    "php-sources",
    "picatic-keys_secrets",
    "mailchimp-keys_secrets",
    "mailgun-keys_secrets",
    "jwt",
    "interestingparams",
    "interestingsubs",
    "ip",
    "stripe-keys_secrets",
    "twitter-oauth",
    "twitter-oauth_secrets",
    "twitter-secret",
    "twitter-token_secrets",
    "facebook-oauth",
    "facebook-oauth_secrets",
    "facebook-token_secrets",
    "debug-pages(1)",
    "debug-pages",
    "debug_logic",
]

# Input file and output file
input_file = "yourjsfile.js"
output_file = "jsfile_results.txt"

# Check if input file exists
if not os.path.exists(input_file):
    print(f"Error: {input_file} not found in the current directory!")
    sys.exit(1)

# Open output file for writing results
with open(output_file, "w") as outfile:
    for pattern in patterns:
        # Run the GF command for each pattern
        try:
            command = f"gf {pattern} {input_file}"
            result = subprocess.run(command, shell=True, capture_output=True, text=True)

            # Write pattern header to output file
            outfile.write(f"--- Pattern: {pattern} ---\n")
            if result.stdout.strip():
                outfile.write(result.stdout + "\n")
            else:
                outfile.write("No matches found.\n")
            outfile.write("\n")

            # Print to CLI if -cli argument is provided
            if "-cli" in sys.argv:
                print(f"--- Pattern: {pattern} ---")
                if result.stdout.strip():
                    print(result.stdout)
                else:
                    print("No matches found.")
                print("\n")
        except Exception as e:
            print(f"Error while processing pattern {pattern}: {e}")

print(f"Scanning completed. Results saved in {output_file}.")

