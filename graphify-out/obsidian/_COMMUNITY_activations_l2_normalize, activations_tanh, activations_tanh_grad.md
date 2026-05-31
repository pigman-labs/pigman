---
type: community
cohesion: 0.04
members: 109
---

# activations_l2_normalize, activations_tanh, activations_tanh_grad

**Cohesion:** 0.04 - loosely connected
**Members:** 109 nodes

## Members
- [[.__init__()_37]] - code - neural/adapter.py
- [[.__init__()_36]] - code - neural/dynamics_model.py
- [[.__init__()_38]] - code - neural/jepa_model.py
- [[.__init__()_40]] - code - neural/layers.py
- [[.__init__()_8]] - code - torch_backend/modules.py
- [[.__init__()_7]] - code - torch_backend/modules.py
- [[.__init__()_6]] - code - torch_backend/modules.py
- [[.__init__()_39]] - code - neural/synthetic_data.py
- [[.__init__()_32]] - code - multimodal_stack/torch_modules.py
- [[.__init__()_34]] - code - multimodal_stack/torch_modules.py
- [[.__init__()_33]] - code - multimodal_stack/torch_modules.py
- [[.__init__()_9]] - code - torch_backend/world_model.py
- [[.__init__()_10]] - code - torch_backend/world_model.py
- [[.__init__()_11]] - code - torch_backend/world_model.py
- [[._copy_context_to_target()]] - code - neural/jepa_model.py
- [[.backward()]] - code - neural/layers.py
- [[.batch()]] - code - neural/synthetic_data.py
- [[.copy()]] - code - dynamics/latent_state.py
- [[.ema_target()]] - code - neural/jepa_model.py
- [[.encode_context()]] - code - neural/jepa_model.py
- [[.encode_target()]] - code - neural/jepa_model.py
- [[.forward()_9]] - code - neural/layers.py
- [[.forward()_2]] - code - torch_backend/modules.py
- [[.forward()_1]] - code - torch_backend/modules.py
- [[.forward()_6]] - code - multimodal_stack/torch_modules.py
- [[.forward()_8]] - code - multimodal_stack/torch_modules.py
- [[.load()]] - code - neural/jepa_model.py
- [[.load_state_dict()]] - code - neural/layers.py
- [[.predict()_1]] - code - neural/jepa_model.py
- [[.predict_delta()]] - code - neural/dynamics_model.py
- [[.save()]] - code - neural/jepa_model.py
- [[.state_dict()]] - code - neural/layers.py
- [[.step()_3]] - code - neural/jepa_model.py
- [[.step()_4]] - code - neural/layers.py
- [[.train_step()]] - code - neural/dynamics_model.py
- [[.train_step()_1]] - code - neural/jepa_model.py
- [[.write()]] - code - tools/filesystem.py
- [[.zero_grad()]] - code - neural/jepa_model.py
- [[.zero_grad()_1]] - code - neural/layers.py
- [[Deterministic linearnonlinear world used to prove the neural loop trains.]] - rationale - neural/synthetic_data.py
- [[JointWorldModelReport]] - code - training/loops/train_joint_world_model.py
- [[Linear]] - code - neural/layers.py
- [[LinearCache]] - code - neural/layers.py
- [[MoEFeedForward]] - code - torch_backend/modules.py
- [[ModalityAdapter]] - code - multimodal_stack/torch_modules.py
- [[MultimodalWorldStack]] - code - multimodal_stack/torch_modules.py
- [[NeuralTrainReport]] - code - training/loops/train_neural_jepa.py
- [[OptimizerConfig]] - code - neural/optim.py
- [[RMSNorm]] - code - torch_backend/modules.py
- [[ResidualMLPBlock]] - code - torch_backend/modules.py
- [[Small but real action-conditioned JEPA trained with manual backprop.]] - rationale - neural/jepa_model.py
- [[SyntheticBatch]] - code - neural/synthetic_data.py
- [[SyntheticWorldDataset]] - code - neural/synthetic_data.py
- [[TinySSMBlock]] - code - multimodal_stack/torch_modules.py
- [[TorchDynamicsReport]] - code - training/loops/train_torch_dynamics.py
- [[TorchEncoder]] - code - torch_backend/world_model.py
- [[TorchJEPAModel]] - code - torch_backend/world_model.py
- [[TorchLatentDynamics]] - code - torch_backend/world_model.py
- [[TorchModelConfig]] - code - torch_backend/config.py
- [[TorchTrainConfig]] - code - torch_backend/config.py
- [[TorchTrainReport]] - code - training/loops/train_torch_jepa.py
- [[TrainStep]] - code - neural/jepa_model.py
- [[TrainableJEPA]] - code - neural/jepa_model.py
- [[TrainableLatentDynamics]] - code - neural/dynamics_model.py
- [[activations.py]] - code - neural/activations.py
- [[checkpoint.py_1]] - code - neural/checkpoint.py
- [[config.py_1]] - code - torch_backend/config.py
- [[device.py]] - code - torch_backend/device.py
- [[dynamics_model.py]] - code - neural/dynamics_model.py
- [[evaluate_checkpoint()]] - code - evals/neural_eval.py
- [[jepa_model.py]] - code - neural/jepa_model.py
- [[l2_normalize()]] - code - neural/activations.py
- [[layers.py]] - code - neural/layers.py
- [[load_npz()]] - code - neural/checkpoint.py
- [[losses.py]] - code - torch_backend/losses.py
- [[main()_3]] - code - scripts/train_joint_world_model.py
- [[main()_6]] - code - scripts/train_neural.py
- [[main()_9]] - code - scripts/train_torch_dynamics.py
- [[main()_2]] - code - scripts/train_torch_jepa.py
- [[modules.py]] - code - torch_backend/modules.py
- [[neural_eval.py]] - code - evals/neural_eval.py
- [[optim.py]] - code - neural/optim.py
- [[save_npz()]] - code - neural/checkpoint.py
- [[seed_everything()]] - code - torch_backend/device.py
- [[select_device()]] - code - torch_backend/device.py
- [[synthetic_data.py]] - code - neural/synthetic_data.py
- [[tanh()]] - code - neural/activations.py
- [[tanh_grad()]] - code - neural/activations.py
- [[test_torch_backend.py]] - code - tests/unit/test_torch_backend.py
- [[test_torch_dynamics_forward_shapes()]] - code - tests/unit/test_torch_backend.py
- [[test_torch_jepa_forward_shapes()]] - code - tests/unit/test_torch_backend.py
- [[test_torch_training_writes_checkpoints()]] - code - tests/unit/test_torch_backend.py
- [[torch_modules.py]] - code - multimodal_stack/torch_modules.py
- [[train_dynamics_torch()]] - code - training/loops/train_torch_dynamics.py
- [[train_jepa_torch()]] - code - training/loops/train_torch_jepa.py
- [[train_joint_world_model()]] - code - training/loops/train_joint_world_model.py
- [[train_joint_world_model.py_1]] - code - scripts/train_joint_world_model.py
- [[train_joint_world_model.py]] - code - training/loops/train_joint_world_model.py
- [[train_neural.py]] - code - scripts/train_neural.py
- [[train_neural_jepa()]] - code - training/loops/train_neural_jepa.py
- [[train_neural_jepa.py]] - code - training/loops/train_neural_jepa.py
- [[train_torch_dynamics.py_1]] - code - scripts/train_torch_dynamics.py
- [[train_torch_dynamics.py]] - code - training/loops/train_torch_dynamics.py
- [[train_torch_jepa.py_1]] - code - scripts/train_torch_jepa.py
- [[train_torch_jepa.py]] - code - training/loops/train_torch_jepa.py
- [[uncertainty_loss()]] - code - torch_backend/losses.py
- [[update_target()]] - code - torch_backend/world_model.py
- [[vicreg_loss()]] - code - torch_backend/losses.py
- [[world_model.py]] - code - torch_backend/world_model.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/activations_l2_normalize,_activations_tanh,_activations_tanh_grad
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_agent_eval_run_agent_eval, agent_loop_agentloop_run, code_codeverifier]]
- 8 edges to [[_COMMUNITY_action_agentaction, action_agentaction_to_record, action_policy_actionpolicy]]
- 7 edges to [[_COMMUNITY_adapter_fixed_width, adapter_neuralworldmodeladapter, adapter_neuralworldmodeladapter_predict_vector]]
- 6 edges to [[_COMMUNITY_alignment_dpo_py, alignment_preferences_py, build_dataset_main]]
- 5 edges to [[_COMMUNITY_episodic_memory_episode, episodic_memory_episodicmemory, episodic_memory_episodicmemory_recent]]
- 2 edges to [[_COMMUNITY_basehttprequesthandler, decoders_text_decoder_py, filesystem_filesystemtool_read]]
- 1 edge to [[_COMMUNITY_evals_planner_eval_py, planner_eval_run_planner_eval, planner_search_py]]
- 1 edge to [[_COMMUNITY_abc, base_encode, base_encoder]]
- 1 edge to [[_COMMUNITY_action_decoder_actiondecoder, action_decoder_actiondecoder_decode, action_decoder_actiondecoder_init]]

## Top bridge nodes
- [[.step()_4]] - degree 12, connects to 5 communities
- [[.write()]] - degree 8, connects to 4 communities
- [[evaluate_checkpoint()]] - degree 10, connects to 3 communities
- [[train_jepa_torch()]] - degree 22, connects to 2 communities
- [[train_dynamics_torch()]] - degree 20, connects to 2 communities