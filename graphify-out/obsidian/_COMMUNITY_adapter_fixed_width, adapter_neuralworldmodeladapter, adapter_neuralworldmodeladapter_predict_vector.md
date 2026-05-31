---
type: community
cohesion: 0.12
members: 29
---

# adapter_fixed_width, adapter_neuralworldmodeladapter, adapter_neuralworldmodeladapter_predict_vector

**Cohesion:** 0.12 - loosely connected
**Members:** 29 nodes

## Members
- [[.__init__()_24]] - code - world_model/world_model.py
- [[.predict()_2]] - code - jepa/predictor.py
- [[.predict()]] - code - world_model/world_model.py
- [[.predict_next()]] - code - dynamics/transition_model.py
- [[.predict_vector()]] - code - neural/adapter.py
- [[DynamicsTrainStats]] - code - training/loops/train_dynamics.py
- [[JEPAPredictor]] - code - jepa/predictor.py
- [[NeuralWorldModelAdapter]] - code - neural/adapter.py
- [[Prediction]] - code - jepa/predictor.py
- [[PretrainStats]] - code - training/loops/pretrain_jepa.py
- [[TransitionModel]] - code - dynamics/transition_model.py
- [[WorldModel]] - code - world_model/world_model.py
- [[WorldModelPrediction]] - code - world_model/world_model.py
- [[adapter.py]] - code - neural/adapter.py
- [[fixed_width()]] - code - neural/adapter.py
- [[main()_5]] - code - scripts/train_smoke.py
- [[predictor.py]] - code - jepa/predictor.py
- [[pretrain_jepa.py]] - code - training/loops/pretrain_jepa.py
- [[run_pretrain_smoke()]] - code - training/loops/pretrain_jepa.py
- [[smoke_eval()]] - code - evals/world_model_prediction.py
- [[test_neural.py]] - code - tests/unit/test_neural.py
- [[test_neural_eval_reads_checkpoint()]] - code - tests/unit/test_neural.py
- [[test_neural_jepa_trains_and_loads()]] - code - tests/unit/test_neural.py
- [[train_dynamics.py]] - code - training/loops/train_dynamics.py
- [[train_dynamics_smoke()]] - code - training/loops/train_dynamics.py
- [[train_smoke.py]] - code - scripts/train_smoke.py
- [[transition_model.py]] - code - dynamics/transition_model.py
- [[world_model.py_1]] - code - world_model/world_model.py
- [[world_model_prediction.py]] - code - evals/world_model_prediction.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/adapter_fixed_width,_adapter_neuralworldmodeladapter,_adapter_neuralworldmodeladapter_predict_vector
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_action_agentaction, action_agentaction_to_record, action_policy_actionpolicy]]
- 7 edges to [[_COMMUNITY_activations_l2_normalize, activations_tanh, activations_tanh_grad]]
- 1 edge to [[_COMMUNITY_episodic_memory_episode, episodic_memory_episodicmemory, episodic_memory_episodicmemory_recent]]
- 1 edge to [[_COMMUNITY_agent_eval_run_agent_eval, agent_loop_agentloop_run, code_codeverifier]]

## Top bridge nodes
- [[.predict_next()]] - degree 7, connects to 2 communities
- [[.predict()_2]] - degree 5, connects to 2 communities
- [[smoke_eval()]] - degree 5, connects to 2 communities
- [[WorldModel]] - degree 10, connects to 1 community
- [[TransitionModel]] - degree 9, connects to 1 community