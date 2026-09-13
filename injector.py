
import logging
import colorlog

'''
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(levelname)s:\t%(asctime)s\t[%(filename)s:%(lineno)d]\t%(message)s'))
logger.addHandler(handler)
'''

# 기본 설정: 로그 레벨을 INFO로 설정하고, 포맷을 지정

class LevelSpecificColorFormatter(logging.Formatter):
    # ANSI 색상 코드 정의
    GREEN = "\033[92m"
    RESET = "\033[0m"

    def format(self, record):
        # 원본 레벨네임 보관 (다른 핸들러나 파일 저장을 위해 훼손 방지)
        orig_levelname = record.levelname
        
        # 오직 INFO 레벨일 때만 'INFO' 텍스트를 초록색으로 감쌈
        if record.levelno == logging.INFO:
            record.levelname = f"{self.GREEN}{record.levelname}{self.RESET}"
            # 만약 메시지 내용까지 초록색으로 하고 싶다면 아래 주석을 해제하세요.
            # record.msg = f"{self.GREEN}{record.msg}{self.RESET}"

        # 포맷 서식 정의 (datetime, filename, levelname, message)
        formatter = logging.Formatter(
            fmt='%(levelname)s:\t%(asctime)s\t[%(filename)s:%(lineno)d]\t%(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        result = formatter.format(record)
        
        # 다른 로깅 작업에 영향을 주지 않도록 복구
        record.levelname = orig_levelname
        return result

# --- 로거 및 핸들러 설정 ---
logger = logging.getLogger("TargetColorLogger")
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(LevelSpecificColorFormatter())
logger.addHandler(stream_handler)

