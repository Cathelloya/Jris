from typing import Any


def escape_cqcode(text: str) -> str:
    return (text
            .replace("&", "&amp;")
            .replace("[", "&#91;")
            .replace("]", "&#93;")
            .replace(",", "&#44;"))


def encode_cqcode(input_dict: dict[str, Any]) -> str:
    cqcode = '[CQ:' + escape_cqcode(str(input_dict['_type']))
    for k, v in input_dict.items():
        if k.startswith('_'):
            continue
        k = escape_cqcode(str(k))
        v = escape_cqcode(str(v))
        cqcode += f',{k}={v}'

    cqcode += ']'

    return cqcode


if __name__ == '__main__':
    print(encode_cqcode({
        "_type": "test",
        "value": "1"
    }))
