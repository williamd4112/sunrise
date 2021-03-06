# ------------------------------------------------------------------------------
#   @author:
#       Tingwu Wang
# ------------------------------------------------------------------------------


def get_mf_config(parser):
    # get the parameters
    parser.add_argument("--value_lr", type=float, default=3e-4)
    parser.add_argument("--value_epochs", type=int, default=20)
    parser.add_argument("--value_network_shape", type=str, default='64,64')
    # parser.add_argument("--value_batch_size", type=int, default=64)
    parser.add_argument("--value_activation_type", type=str, default='tanh')
    parser.add_argument("--value_normalizer_type", type=str, default='none')

    parser.add_argument("--trust_region_method", type=str, default='trpo',
                        help='["ppo", "trpo"]')
    parser.add_argument("--gae_lam", type=float, default=0.95)
    parser.add_argument("--fisher_cg_damping", type=float, default=0.1)
    parser.add_argument("--target_kl", type=float, default=0.01)
    parser.add_argument("--cg_iterations", type=int, default=10)

    parser.add_argument("--ppo_clip", type=float, default=0.1)
    parser.add_argument("--num_minibatches", type=int, default=10)
    parser.add_argument("--target_kl_high", type=float, default=2)
    parser.add_argument("--target_kl_low", type=float, default=0.5)
    parser.add_argument("--use_weight_decay", type=int, default=0)
    parser.add_argument("--weight_decay_coeff", type=float, default=1e-5)

    parser.add_argument("--use_kl_penalty", type=int, default=0)
    parser.add_argument("--kl_alpha", type=float, default=1.5)
    parser.add_argument("--kl_eta", type=float, default=50)

    parser.add_argument("--policy_lr_schedule", type=str, default='linear',
                        help='["linear", "constant", "adaptive"]')
    parser.add_argument("--policy_lr_alpha", type=int, default=2)
    return parser
