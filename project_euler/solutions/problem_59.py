from typing import List

from ..framework.load_file import load_file


def xor_printable(encrypted: List[int]) -> List[str]:
    allowable_secrets = []
    length = len(encrypted)

    for secret in range(ord('a'), ord('z') + 1):
        decrypted = [chr(c ^ secret) for c in encrypted]

        if any(not c.isprintable() for c in decrypted):
            continue

        if sum(1 for c in decrypted
               if c.isalpha() or c.isspace()) < length * 0.8:
            continue

        allowable_secrets.append(secret)

    return allowable_secrets


def solve(name: str='cipher.txt', relative: bool=True,
          codeword_length: int=3) -> int:
    encrypted_raw = load_file(59, name, relative)

    encrypted = [int(character) for character in encrypted_raw.split(',')]

    allowable_secrets = [xor_printable(encrypted[i::3])
                         for i in range(codeword_length)]

    for i in range(codeword_length):
        assert len(allowable_secrets[i]) == 1

    secret = [secrets[0] for secrets in allowable_secrets]
    decrypted = [chr(c ^ secret[i % 3]) for i, c in enumerate(encrypted)]

    return sum(ord(c) for c in decrypted)
