from hacksport.problem import ProtectedFile, Remote

class Problem(Remote):
	program_name = "bad-exec.py"
	files = [ProtectedFile("flag")]

		
