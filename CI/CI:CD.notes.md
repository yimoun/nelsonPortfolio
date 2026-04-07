# Github Actions
**Code Deployment (CI\CD)**
    A workflow Automation Service by GitHub: All kinds of repository-related processes & actions.
    GitHub Actions makes setting up, configuring and running such CI/CD workflows a breeze. It makes it very easy for setting up processes that do automatically build, test, and publish new versions.
**code and repository management**
    Automate code review, issue management, etc.

# CI/CD
Code deployment: Automate code testing building & deployment

# CI(Continuous Integration)
Code changes are automatically built, tested & merged with existing code.
# CD(Continuous Delivery)
After integration, new app or package versions are published automatically

# GitHub Actions Alternatives (for CI/CD)
**Jenkins**  **GitLab CI/CD**   **Azure Pipeline** **AWS CodePipeline**

# Alternatives of GitHub
GitLab, BitBucket

# GitHUb Actions Key Elements
**Workflows**: Attached to a GitHub repository...contain one or more **Jobs**...Triggered upon **Events** 
**Jobs**: Define a **Runner(Execution envionment)**...Contain one or more **Steps**...Run in parallel(default) or sequential Can be conditional
**Steps**: Execute a shell script or an Action...

# Events (Workflow Triggers)
**Repository-related**: push/pull_request/create/fork/issues/watch/discussion/issue_comment/
**Other**: Workflow_dispatch(Manually trigger workflow)/repository_dispatch(REST API request triggers workflow)/schedule (Workflow is scheduled)/Workflow_call (Can be call by other workflows).

# What are Actions ?
**Action** is a (custom) application that perfoms a (typically complex) frequently repeated task. It's useful when you don't have to use a run command. You can build your own Actions but you can also use official or community Actions (for example **GitHub Action Checkout**).
Example of List of Steps belong in a "test" job:
1. Get code (using the GitHub Action Checkout )
2. Install NodeJS (using the action/setup-node@v3)
3. Install dependencies (using a runn command)
4. Run tests (using a run command)