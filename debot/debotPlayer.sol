pragma ton-solidity >=0.35.0;
pragma AbiHeader expire;
pragma AbiHeader time;
pragma AbiHeader pubkey;

import "./Debot.sol";


contract DebotPlayer is Debot {
    bytes m_icon;

    function setIcon(bytes icon) public {
        require(msg.pubkey() == tvm.pubkey(), 100);
        tvm.accept();
        m_icon = icon;
    }

    function start() public override {}

    function getRequiredInterfaces() public view override returns (uint256[] interfaces) {
        return [uint256(0)];
    }

    function getDebotInfo() public functionID(0xDEB) override view returns(
        string name, string version, string publisher, string caption, string author,
        address support, string hello, string language, string dabi, bytes icon
    ) {
        name = "DebotPlayer";
        version = "0.2.0";
        publisher = "ICT_HACK";
        caption = "Play with me";
        author = "Sad, but tasty";
        support = address.makeAddrStd(0, 0x965b5cab2d3e6db7a5ded3ea6822ff5c6fcba27e75b0fd3fc30836de2fb6be80);
        hello = "Hello, I am a DebotPlayer!";
        language = "en";
        dabi = m_debotAbi.get();
        icon = m_icon;
    }

    function compareResults(uint a, uint b) public pure returns (int) {
        int res = 0;

        if (a > b) {
            res = 1;
        } else if (a < b) {
            res = -1;
        }

        return res;
    }

    function guessNumber() public view returns (uint) {
        return random();
    }

    function random() private view returns (uint) {
        return now % 6 + 1;
    }
}