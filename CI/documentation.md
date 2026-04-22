# Workflows:can be triggered manually or according to a defined schedule.
Each capable of performing a different set of tasks, such as:
    -->Build and test the draw requests
    -->Deploy your application each time a version is created
    -->Adding a label each time a new issue is opened


# Events 
They can also trigger workflow execution based **on a schedule** , by **publishing to a REST API** , or **manually**.


# Jobs
You can also use a **matrix** to run the same job multiple times, each with a different combination of variables, such as operating systems or language versions.

# Action
They can perform tasks such as:
    -->Extracting your Git repository from GitHub
    -->Configure the appropriate toolchain for your build environment
    -->Configure authentication with your cloud provider

# Tests for CI
Your tests may include code analyzers (which check formatting), security checks, code coverage, functional tests, and other custom checks.

# Varibales: Default variable / custom (environment / configuration) variable.
**Defining environment variables for a single workflow**
You can use either runner environment variables or contexts in run steps, but in the parts of a workflow that are not sent to the runner you must use contexts to access variable values.
**Defining configuration variables for multiple workflows**
 either the organization, repository, or environment level.

# Contexts are a way to access information about workflow runs, variables, runner environments, jobs, and steps.
I have read in detail when to use each of the following contexts: “github”, “env”, “vars”, “job”, “jobs”, “steps”, “runner”, “secrets”, “strategy”, “matrix”, ‘needs’, and “inputs”

# Reference/Workflow syntax for GitHub Actions


# Important
--> Default environment variables exist only on the task executor. Most contexts are useful at any stage of the workflow, including when default variables are not available. For example, contexts are useful for performing initial processing before the task is routed to an executor.
--> When creating workflows and actions, you must always determine whether your code could execute untrusted inputs from potentially malicious actors. Certain contexts must be treated as untrusted inputs, as an attacker could inject their own malicious content into them.
--> If possible, store values in variables and avoid hard-coding values. However, you will need to define these variables at the appropriate levels (environment, configuration).
