const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const mongoose = require('mongoose');
const tasksRouter = require('./routes/tasks');

const app = express();
app.use(bodyParser.json());
app.use(cors());

// en localParser: true,
//   useUnifiedTopology: true,
// mongoose.connect('mongodb://localhost:27017/todoapp', {
//   useNewUrl
// });
// container

mongoose.connect('mongodb://mongo:27017/todoapp', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

app.use('/tasks', tasksRouter);

app.get('/', (req, res) => {
  res.send('Bienvenue sur l\'API TODO');
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Backend listening on port ${PORT}`);
});
