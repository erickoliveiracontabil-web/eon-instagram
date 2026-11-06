import json, base64, sys
d = json.load(open(sys.argv[1]))
print({k: v for k, v in d.items() if k not in ("audio_base64", "url")})
open(sys.argv[2], "wb").write(base64.b64decode(d["audio_base64"]))
