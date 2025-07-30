---
name: local_authority_net_zero_commitments
title: Local authority net zero commitments
description: "Dataset of net zero promises made by local authorities, including their\
  \ scope and timeline\n"
version: latest
licenses:
- name: CC-BY-4.0
  path: https://creativecommons.org/licenses/by/4.0/
  title: Creative Commons Attribution 4.0 International License
contributors:
- title: mySociety
  path: https://mysociety.org
  role: author
- title: Climate Emergency UK
  path: https://www.climateemergency.uk/
  role: author
custom:
  build: la_plans_promises.build:build_commitments
  tests:
  - test_local_authority_net_zero_commitments
  dataset_order: 0
  download_options:
    gate: default
    survey: default
    header_text: default
  composite:
    xlsx:
      include: all
      exclude: none
      render: true
    sqlite:
      include: all
      exclude: none
      render: true
    json:
      include: all
      exclude: none
      render: true
  change_log:
    0.1.0: Initial commit of data
    0.1.1: 'Minor change in data for resource(s): promises'
    0.2.0: 'Change in data for resource(s): promises'
    0.3.0: 'Change in data for resource(s): promises'
    0.3.1: 'Minor change in data for resource(s): promises'
    0.4.0: 'New field(s) added to resource: data_checked'
    0.4.1: 'Minor change in data for resource(s): promises'
    0.4.2: 'Minor change in data for resource(s): promises'
    0.4.3: 'Minor change in data for resource(s): promises'
    0.4.4: 'Minor change in data for resource(s): promises'
    0.4.5: 'Minor change in data for resource(s): promises'
    0.5.0: 'Change in data for resource(s): promises'
    0.6.0: 'Change in data for resource(s): promises'
    0.6.1: 'Minor change in data for resource(s): promises'
  datasette:
    about: Info & Downloads
    about_url: https://mysociety.github.io/la_plans_promises/datasets/local_authority_net_zero_commitments/0_6_1
  formats:
    csv: true
    parquet: true
resources:
- title: Local authority net zero commitments
  description: Dataset of net zero promises made by local authorities, including their
    scope and timeline
  custom:
    row_count: 496
    datasette:
      about: Info & Downloads
      about_url: https://mysociety.github.io/la_plans_promises/datasets/local_authority_net_zero_commitments/0_6_1#promises
  path: promises.csv
  name: promises
  profile: tabular-data-resource
  scheme: file
  format: csv
  hashing: md5
  encoding: utf-8
  schema:
    fields:
    - name: local-authority-code
      type: string
      description: 3/4 letter code for local authority (see https://mysociety.github.io/uk_local_authority_names_and_codes/)
      constraints:
        unique: false
      example: ABC
    - name: council
      type: string
      description: Name of council
      constraints:
        unique: false
      example: Aberdeen City Council
    - name: scope
      type: string
      description: Does the emissions reduction target apply to just council or to
        all activity in the area?
      constraints:
        unique: false
        enum:
        - Council operations
        - No promise
        - Other
        - Unclear
        - Whole area
      example: Council operations
    - name: target
      type: number
      description: Target year for net zero
      constraints:
        unique: false
      example: 2023.0
    - name: wording
      type: string
      description: Exact wording of promise
      constraints:
        unique: false
      example: "\nAchieving a carbon neutral Wokingham Borough \nby 2030."
    - name: source_url
      type: string
      description: Where promise was found
      constraints:
        unique: false
      example: http://applications.huntingdonshire.gov.uk/moderngov/documents/s117768/Environment%20Principles%20Report.pdf
    - name: source_name
      type: string
      description: Website page name where promise was found
      constraints:
        unique: false
      example: 2020 Climate Action Framework | Cherwell District Council
    - name: data_checked
      type: string
      description: When this plan was last checked
      constraints:
        unique: false
      example: 20/11/23
    - name: notes
      type: string
      description: Additional notes on council or promise
      constraints:
        unique: false
      example: '"The UK government is at forefront of this battle, having signed into
        legislation June 2019 a commitment to become carbon neutral by 2050. As such,
        Bassetlaw District Council will be working hand-in-hand with other Local Authorities
        and businesses to reduce our emission and supporting the national agenda."'
    - name: gss_code
      type: string
      description: GSS code for this local authority
      constraints:
        unique: false
      example: E06000001
    - name: region
      type: string
      description: Region of this local authority
      constraints:
        unique: false
      example: East Midlands
    - name: local-authority-type-name
      type: string
      description: Type of local authority
      constraints:
        unique: false
      example: City corporation
    - name: county-la
      type: string
      description: County of this local authority
      constraints:
        unique: false
      example: CAM
    - name: combined-authority
      type: string
      description: Combined authority of this local authority
      constraints:
        unique: false
      example: CPCA
  hash: 334b3bc21ec5a500a2459ae986319816
full_version: 0.6.1
permalink: /datasets/local_authority_net_zero_commitments/latest
---
