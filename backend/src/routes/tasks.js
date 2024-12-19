const express = require('express');
const router = express.Router();
const Task = require('../models/task');

// Récupérer toutes les tâches
router.get('/', async (req, res) => {
  const tasks = await Task.find({});
  res.json(tasks);
});

// Créer une nouvelle tâche
router.post('/', async (req, res) => {
  const { title } = req.body;
  const newTask = new Task({ title });
  await newTask.save();
  res.json(newTask);
});

// Mettre à jour une tâche (par ex. la marquer faite)
router.put('/:id', async (req, res) => {
  const { id } = req.params;
  const { done } = req.body;
  const updatedTask = await Task.findByIdAndUpdate(id, { done }, { new: true });
  res.json(updatedTask);
});

// Supprimer une tâche
router.delete('/:id', async (req, res) => {
  const { id } = req.params;
  await Task.findByIdAndDelete(id);
  res.json({ message: 'Task deleted' });
});

module.exports = router;
