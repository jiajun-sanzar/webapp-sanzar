# import ee

# The service account email address authorized by your Google contact.
# Set up a service account as described in the README.
# EE_ACCOUNT = 'user@mail.com'

# The private key associated with your service account in Privacy Enhanced
# Email format (.pem suffix).  To convert a private key from the RSA format
# (.p12 suffix) to .pem, run the openssl command like this:
# openssl pkcs12 -in downloaded-privatekey.p12 -nodes -nocerts > privatekey.pem
# https://cloud.google.com/iam/docs/creating-managing-service-account-keys
# Install the Gclould, then in the command line generated the private key
# gcloud iam service-accounts keys create KEY_FILE --iam-account=SERVICE_ACCOUNT
# Before intalling the gclould sdk check the following page
# https://cloud.google.com/sdk/docs/configurations?hl=es-419
# EE_PRIVATE_KEY_FILE = 'credentials/privatekey.pem'

# EE_CREDENTIALS = ee.ServiceAccountCredentials(EE_ACCOUNT, EE_PRIVATE_KEY_FILE)