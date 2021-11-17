import web3

address = web3.Web3().toChecksumAddress("0x95066025af40f7f7832f61422802cd1e13c23753")
ABI = [
    {
        "inputs": [
            {"internalType": "address", "name": "_WAGMI", "type": "address"},
            {"internalType": "address", "name": "_sWAGMI", "type": "address"},
            {"internalType": "uint32", "name": "_duration", "type": "uint32"},
            {"type": "uint256", "name": "_firstEpochNumber", "internalType": "uint256"},
            {"name": "_firstEpochTime", "internalType": "uint32", "type": "uint32"},
        ],
        "stateMutability": "nonpayable",
        "type": "constructor",
    },
    {
        "inputs": [
            {
                "type": "address",
                "internalType": "address",
                "name": "previousOwner",
                "indexed": True,
            },
            {
                "type": "address",
                "name": "newOwner",
                "indexed": True,
                "internalType": "address",
            },
        ],
        "type": "event",
        "name": "OwnershipTransferred",
        "anonymous": False,
    },
    {
        "name": "WAGMI",
        "type": "function",
        "inputs": [],
        "outputs": [{"name": "", "type": "address", "internalType": "address"}],
        "stateMutability": "view",
        "constant": True,
        "signature": "0x5deb9fc7",
    },
    {
        "name": "distributor",
        "outputs": [{"type": "address", "name": "", "internalType": "address"}],
        "inputs": [],
        "stateMutability": "view",
        "type": "function",
        "constant": True,
        "signature": "0xbfe10928",
    },
    {
        "type": "function",
        "inputs": [],
        "outputs": [
            {"name": "number", "type": "uint256", "internalType": "uint256"},
            {"internalType": "uint256", "type": "uint256", "name": "distribute"},
            {"type": "uint32", "name": "duration", "internalType": "uint32"},
            {"type": "uint32", "name": "endTime", "internalType": "uint32"},
        ],
        "name": "epoch",
        "stateMutability": "view",
        "constant": True,
        "signature": "0x900cf0cf",
    },
    {
        "name": "locker",
        "inputs": [],
        "type": "function",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "constant": True,
        "signature": "0xd7b96d4e",
    },
    {
        "type": "function",
        "inputs": [],
        "name": "policy",
        "stateMutability": "view",
        "outputs": [{"type": "address", "name": "", "internalType": "address"}],
        "constant": True,
        "signature": "0x0505c8c9",
    },
    {
        "type": "function",
        "name": "pullPolicy",
        "stateMutability": "nonpayable",
        "inputs": [],
        "outputs": [],
    },
    {
        "name": "pushPolicy",
        "inputs": [
            {"type": "address", "name": "newPolicy_", "internalType": "address"}
        ],
        "stateMutability": "nonpayable",
        "outputs": [],
        "type": "function",
    },
    {
        "name": "renouncePolicy",
        "outputs": [],
        "type": "function",
        "inputs": [],
        "stateMutability": "nonpayable",
    },
    {
        "stateMutability": "view",
        "inputs": [],
        "type": "function",
        "name": "sWAGMI",
        "outputs": [{"name": "", "type": "address", "internalType": "address"}],
        "constant": True,
        "signature": "0x3a307949",
    },
    {
        "name": "totalBonus",
        "type": "function",
        "stateMutability": "view",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "inputs": [],
        "constant": True,
        "signature": "0xa8dd07dc",
    },
    {
        "type": "function",
        "stateMutability": "view",
        "name": "warmupContract",
        "inputs": [],
        "outputs": [{"type": "address", "name": "", "internalType": "address"}],
        "constant": True,
        "signature": "0xed4acaa8",
    },
    {
        "name": "warmupInfo",
        "inputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "outputs": [
            {"name": "deposit", "type": "uint256", "internalType": "uint256"},
            {"type": "uint256", "name": "gons", "internalType": "uint256"},
            {"name": "expiry", "type": "uint256", "internalType": "uint256"},
            {"internalType": "bool", "name": "lock", "type": "bool"},
        ],
        "type": "function",
    },
    {
        "type": "function",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "inputs": [],
        "name": "warmupPeriod",
        "stateMutability": "view",
        "constant": True,
        "signature": "0xdeac361a",
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "name": "stake",
        "inputs": [
            {"internalType": "uint256", "name": "_amount", "type": "uint256"},
            {"name": "_recipient", "type": "address", "internalType": "address"},
        ],
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
    },
    {
        "name": "claim",
        "stateMutability": "nonpayable",
        "type": "function",
        "outputs": [],
        "inputs": [
            {"type": "address", "name": "_recipient", "internalType": "address"}
        ],
    },
    {
        "stateMutability": "nonpayable",
        "outputs": [],
        "type": "function",
        "inputs": [],
        "name": "forfeit",
    },
    {
        "name": "toggleDepositLock",
        "stateMutability": "nonpayable",
        "type": "function",
        "inputs": [],
        "outputs": [],
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "outputs": [],
        "inputs": [
            {"internalType": "uint256", "name": "_amount", "type": "uint256"},
            {"internalType": "bool", "name": "_trigger", "type": "bool"},
        ],
        "name": "unstake",
    },
    {
        "stateMutability": "view",
        "type": "function",
        "inputs": [],
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "name": "index",
        "constant": True,
        "signature": "0x2986c0e5",
    },
    {
        "outputs": [],
        "name": "rebase",
        "type": "function",
        "stateMutability": "nonpayable",
        "inputs": [],
    },
    {
        "outputs": [{"internalType": "uint256", "type": "uint256", "name": ""}],
        "type": "function",
        "name": "contractBalance",
        "stateMutability": "view",
        "inputs": [],
        "constant": True,
        "signature": "0x8b7afe2e",
    },
    {
        "name": "giveLockBonus",
        "stateMutability": "nonpayable",
        "inputs": [{"internalType": "uint256", "type": "uint256", "name": "_amount"}],
        "type": "function",
        "outputs": [],
    },
    {
        "stateMutability": "nonpayable",
        "type": "function",
        "outputs": [],
        "name": "returnLockBonus",
        "inputs": [{"type": "uint256", "name": "_amount", "internalType": "uint256"}],
    },
    {
        "name": "setContract",
        "outputs": [],
        "inputs": [
            {
                "name": "_contract",
                "type": "uint8",
                "internalType": "enum Staking.CONTRACTS",
            },
            {"type": "address", "internalType": "address", "name": "_address"},
        ],
        "type": "function",
        "stateMutability": "nonpayable",
    },
    {
        "name": "setWarmup",
        "inputs": [
            {"internalType": "uint256", "name": "_warmupPeriod", "type": "uint256"}
        ],
        "stateMutability": "nonpayable",
        "outputs": [],
        "type": "function",
    },
]
