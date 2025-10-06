import asyncio

async def wczytywanie(nazwaPliku: str) -> None:
    print(f"Wczytywanie pliku {nazwaPliku}")
    await asyncio.sleep(2)
async def analiza(nazwaPliku: str) -> None:
    print(f"Analiza pliku {nazwaPliku}")
    await asyncio.sleep(4)

async def zapisywanie(nazwaPliku: str) -> None:
    print(f"Zapisywanie pliku {nazwaPliku}")
    await asyncio.sleep(1)

async def przetwarzanie(nazwaPliku: str) -> None:
    await wczytywanie(nazwaPliku)
    await analiza(nazwaPliku)
    await zapisywanie(nazwaPliku)

async def main() -> None:
    await asyncio.gather(przetwarzanie("obraz1.png"), przetwarzanie("obraz2.png"))


if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())
