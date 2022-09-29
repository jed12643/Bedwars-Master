on:
  push:
    branches:
    - main
    - release/*
    
on:
  pull_request:
    branches:
    - main
    
on:
  schedule:
  - cron: "0 2 * * 1-5"
  
on:
  workflow_dispatch:
    
jobs:
  my_job:
    name: deploy to staging
    runs-on: ubuntu-18.04
    
- name: Setup Node
  uses: actions/setup-node@v1
  with:
    node-version: '10.x'
    
    - name: Install Dependencies
  run: npm install
  
 jobs:
   test:
    name: Test on node ${{ matrix.node_version }} and ${{ matrix.os }}
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        node_version: ['8', '10', '12']
        os: [ubuntu-latest, windows-latest, macOS-latest]

    steps:
    - uses: actions/checkout@v1
    - name: Use Node.js ${{ matrix.node_version }}
      uses: actions/setup-node@v1
      with:
        node-version: ${{ matrix.node_version }}

    - name: npm install, build and test
      run: |
        npm install
        npm run build --if-present
        npm test
        
        steps:
      - run: npm publish
        if: github.event_name == 'push'
