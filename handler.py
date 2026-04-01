import os
import pathlib

VOLUME = "/runpod-volume"
WORKSPACE = "/workspace"

def init_storage():
    os.makedirs(VOLUME, exist_ok=True)
    os.makedirs(f"{VOLUME}/models", exist_ok=True)
    os.makedirs(f"{VOLUME}/output", exist_ok=True)
    os.makedirs(f"{VOLUME}/input", exist_ok=True)

    # Symlink /workspace -> /runpod-volume (optional, theo yêu cầu của bạn)
    if os.path.islink(WORKSPACE) or os.path.exists(WORKSPACE):
        try:
            # không xoá nếu là thư mục quan trọng; chỉ symlink nếu bạn chắc
            pass
        except:
            pass

    # cách an toàn hơn: tạo thư mục làm việc bên trong volume thay vì ép /workspace
    # nhưng nếu bạn muốn đúng /workspace:
    if not os.path.islink(WORKSPACE):
        try:
            if os.path.isdir(WORKSPACE):
                # nếu /workspace có sẵn, bạn có thể bỏ qua symlink và dùng VOLUME trực tiếp
                return
            if os.path.exists(WORKSPACE):
                return
            os.symlink(VOLUME, WORKSPACE)
        except Exception:
            # fallback: cứ dùng /runpod-volume
            return
