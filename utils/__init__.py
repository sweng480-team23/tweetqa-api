from controllers import app
from tqa_training_lib.model_runners.tf_bert_model_runner import TFBertModelRunner

import sys

if '--skip-runner' in sys.argv or app.app.config['TESTING']:
    tf_runner_best = None
    print('******** Skip runner or testing flag detected. Won\'t attempt to instantiate a runner.')
    print('******** Note that this will not allow predictions to work right now.')
    print('******** Todo: Create a mock runner subclass that can be used for testing.')
else:
    tf_runner_best = TFBertModelRunner('utils/models/bert_tf/v1/', 'bert-large-uncased-whole-word-masking-finetuned-squad')
