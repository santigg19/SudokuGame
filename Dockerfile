FROM python:3

RUN git clone https://github.com/santigg19/SudokuGame
WORKDIR /SudokuGame

RUN pip install -r requirements.txt
RUN pip install parameterized

CMD [ "python3", "test_interfaz.py" ]