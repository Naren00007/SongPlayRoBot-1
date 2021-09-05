import os
API_ID = int(os.getenv("6801022"))
API_HASH = os.getenv("be0eaa259f93e980a79e1f03996260b4")
BOT_TOKEN = os.getenv("1967644033:AAF_GQdsZ_fKZj-NwS_U1D3jsDBHSjUsqj8")
DATABASE_URL = os.getenv("DATABASE_URL")
OWNER_ID = list({int(x) for x in os.environ.get("609517172", "").split()})
