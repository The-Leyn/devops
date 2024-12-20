const express = require('express');
const router = express.Router();
const Task = require('../models/task');

// Select all
router.get('/', async (req, res) => {
  const tasks = await Task.find({});
  res.json(tasks);
});

// Add
router.post('/', async (req, res) => {
  const { title } = req.body;
  const newTask = new Task({ title });
  await newTask.save();
  res.json(newTask);
});

// Update
router.put('/:id', async (req, res) => {
  const { id } = req.params;
  const { done } = req.body;
  const updatedTask = await Task.findByIdAndUpdate(id, { done }, { new: true });
  res.json(updatedTask);
});

// Delete
router.delete('/:id', async (req, res) => {
  const { id } = req.params;
  await Task.findByIdAndDelete(id);
  res.json({ message: 'Task deleted' });
});

module.exports = router;
