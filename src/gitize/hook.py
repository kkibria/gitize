from prj_gen.common import get_license
from prj_gen.generator import PARAM_TARGET, Gen

from .external import run_cmd


class MyGen(Gen):
    @classmethod
    def pre_process(cls, ctx, params):
        run_cmd("poetry", params[PARAM_TARGET])
        if not params["force"]:
            run_cmd("git", params[PARAM_TARGET])
        ctx["__user__"] = run_cmd("user", None)
        ctx["__email__"] = run_cmd("email", None)
        if ctx['licfile']:
            get_license(params[PARAM_TARGET], params["app"])

    @classmethod
    def post_process(cls, ctx, params):
        ctx["post_injected"] = "post_injected_value"