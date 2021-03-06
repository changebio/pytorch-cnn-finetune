import numpy as np
import torch


def assert_equal_model_outputs(input_var, model1, model2):
    model1.eval()
    model2.eval()
    model1_output = model1(input_var)
    model2_output = model2(input_var)
    assert torch.equal(model1_output, model2_output)


def assert_almost_equal_model_outputs(input_var, model1, model2):
    model1.eval()
    model2.eval()
    model1_output = model1(input_var)
    model2_output = model2(input_var)
    assert np.all(
        np.isclose(
            model1_output.data.numpy(),
            model2_output.data.numpy(),
            rtol=1e-04,
            atol=1e-06,
        )
    )


def copy_module_weights(from_module, to_module):
    to_module.weight.data.copy_(from_module.weight.data)
    to_module.bias.data.copy_(from_module.bias.data)
