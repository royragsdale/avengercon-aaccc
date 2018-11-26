from hacksport.problem_templates import CompiledBinary

Problem = CompiledBinary(sources=["myproblem.c"], flag_file="key", aslr=True, remote=True)
