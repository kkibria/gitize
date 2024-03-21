from prj_gen.generator import Gen
from .external import run_cmd

class MyGen(Gen):
    def pre_process(cls, ctx, params):
        print(params)
        run_cmd("poetry", params["path"])
        run_cmd("git", params["path"])
        ctx["pre_injected"] = "pre_injected_value"

    def post_process(cls, ctx, params):
        ctx["post_injected"] = "post_injected_value"

