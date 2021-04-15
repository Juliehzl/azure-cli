Bump Version Pipeline Usage
=========================

As a prerequisite, please contact Carl Shipley first for the [PLR](http://aka.ms/plrcriteria) (Product Launch Readiness) process.

Then reach out to `azpycli@microsoft.com` to get the CLI onboarding process started. You'll be assigned a dev contact on the CLI team. Early and frequent communication with this contact is essential to ensuring a smooth onboarding.

Here are several typical scenarios to use the pipeline:
### Bump Package Version
#### Input
- PACKAGE_NAME: e.g. azure-mgmt-sql
- PACKAGE_VERSION

### Bump Resource Type Version
#### Input
- RESOURCE_TYPE: e.g. MGMT_STORAGE
- API_VERSION: e.g. 2021-02-01

### Bump Package Version and Resource Type API version
#### Input
- PACKAGE_NAME
- PACKAGE_VERSION
- RESOURCE_TYPE: e.g. MGMT_STORAGE
- API_VERSION: e.g. 2021-02-01

### Bump Package Version and Operation Group API Version
#### Input
- PACKAGE_NAME
- PACKAGE_VERSION
- RESOURCE_TYPE: e.g. MGMT_COMPUTE.virtual_machine_scale_sets
- API_VERSION: e.g. 2021-02-01

### Continue Work on an existing PR
#### Input
The same input for the first request and we will use the existing PR to continue testing