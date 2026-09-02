# 1장 · 컴퓨터 시스템으로의 여행 (A Tour of Computer Systems)

> CSAPP(컴퓨터 시스템 제3판) 1장을 읽으며 정리한 상세 노트. 하드웨어 개념을 백엔드(Spring Boot·FastAPI) 실무에 연결해가며 정리했다.

## 읽는 순서

| # | 글 | 한 줄 요약 |
|---|---|---|
| 01 | [버퍼 오버플로우](01-buffer-overflow.md) | "코드와 데이터가 같은 메모리에 산다"는 대전제 → 스택 스매싱 → 웜 |
| 02 | [프로그램 번역 (컴파일 4단계)](02-program-translation.md) | `hello.c` → 전처리·컴파일·어셈블·링크. `.i/.s/.o` 직접 관찰 |
| 03 | [프로세서와 인스트럭션](03-processor-instructions.md) | 인스트럭션(적재·저장·연산·점프), PC 움직임, 버스·I/O브릿지·DMA |
| 04 | [저장장치 계층과 캐시](04-storage-hierarchy-cache.md) | L0~L6 계층, 지역성, Redis 캐싱(장바구니·최근 본 상품) |
| 05 | [백엔드가 하드웨어에서 실행되는 원리](05-backend-on-hardware.md) | 프로세스·스레드·메모리·디스크를 실제 프로젝트에 대입 |
| 06 | [하드웨어 위의 백엔드 (그림 정리판)](06-hardware-backend-visual.md) | 05를 다이어그램 중심으로 압축한 복습용 |

- **이론 흐름:** 01 → 02 → 03 → 04
- **실무 종합·복습:** 05 → 06

## 폴더 구성
- `assets/` — 그림 (PNG + 원본 SVG)
- `code/hello/` — 컴파일 4단계 실습 코드 (`hello.c`, `hello.i`, `hello.s`, `hello.o`, 실행파일)
