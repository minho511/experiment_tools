from datetime import datetime
import logging
import os

log_path = "path to log folder"

if not os.path.exists(log_path):
    os.makedirs(log_path)

# 기본 로거를 가져오고, 로그 레벨을 INFO로 설정 - INFO 이상의 레벨(즉, WARNING, ERROR, CRITICAL)의 로그 메시지만 기록
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# 기존의 핸들러가 있다면 모두 제거, 새로운 설정으로 다시 시작
if logger.hasHandlers():
    logger.handlers.clear()

# 로그 파일의 이름을 현재 날짜와 시간으로 설정
now = datetime.now()
file_handler = logging.FileHandler(f"logs/{now.strftime('%Y-%m-%d %H:%M:%S')}.log")

# 스트림 핸들러 설정: 로그 메시지를 콘솔에 출력
stream_handler = logging.StreamHandler()

# 포매터 설정: 로그 메시지의 형식을 설정. (로그의 시간, 레벨, 메시지를 포함)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# 핸들러 추가: 파일 핸들러와 스트림 핸들러를 로거에 추가하여 로그 메시지를 파일과 콘솔 모두에 기록
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


# write log
logger.info("contents")