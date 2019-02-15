var express = require('express');
var path = require('path');
// import mongoose from 'mongoose';
var bodyParser = require('body-parser')
var dotenv = require('dotenv')
// import Promise from 'bluebird';
var spawn = require('child_process').spawn;

dotenv.config();
var app = express();
app.use(bodyParser.json());

app.post('/api/tweet', function(req, res) {
  var pythonProcess = spawn('python',['../../model-production/run.py', req.body.data.search]);
  pythonProcess.stdout.on('data', function(data) {
    // console.log(data.toString())
    var output = data.toString()
    output = output.split('\n')
    console.log('output: ' + output[0])
    // console.log('output: ' + output[1])
    res.status(200).json({ response: output[0] })
  });
})

app.get('/api', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(8000, () => console.log('Running on localhost:8000'));
