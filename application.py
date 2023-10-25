import traceback

from app.api.userData.views import *
from config import *


@app.route('/')
def home():
    try:
        return success(message="success",content="Hello World!!")
    except Exception as err:
        print(traceback.print_exc())
        return failure(message="failure",content=str(err))


if __name__ == "__main__":
    app.run(debug=True)
