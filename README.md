# mbot_ip_registry #

### About ###

This is a template repository for setting up your own mbot registry

### Instructions ###

1. Create a GitHub account for your mbot fleet (you will probably also need to create a new email account as GitHub only allows one account per email)

2. Copy this template repository using the GitHub account

3. Add a personal access token to read/write to the repo
    a. Go to Settings > Developer Settings > Personal access tokens
    b. Generate a new Classic token and select repo_deployment as the scope
    c. Set the token to expire never (or some date after you'll need it)
    d. Save the generated token in a safe space, you will not be able to see it again.

4. Edit your mbot_config.txt to use the github username, address of the repo and generated token.
