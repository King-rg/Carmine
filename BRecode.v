// This is the top level for BRecode_tb.v

module BRecodeBlock (
    input [2:0] in,
    output [2:0] out
);
    assign out = (in == 3'b000) ? 3'b000 :
                 (in == 3'b001) ? 3'b001 :
                 (in == 3'b010) ? 3'b001 :
                 (in == 3'b011) ? 3'b010 :
                 (in == 3'b100) ? 3'b110 :
                 (in == 3'b101) ? 3'b101 :
                 (in == 3'b110) ? 3'b101 :
                 (in == 3'b111) ? 3'b000 :
                 3'b000;
endmodule

module BRecode (
    input clk,
    input [31:0] inp,
    output reg [2:0] blockOne,
    output reg [2:0] blockTwo,
    output reg [2:0] blockThree,
    output reg [2:0] blockFour,
    output reg [2:0] blockFive,
    output reg [2:0] blockSix,
    output reg [2:0] blockSeven,
    output reg [2:0] blockEight,
    output reg [2:0] blockNine,
    output reg [2:0] blockTen,
    output reg [2:0] blockEleven,
    output reg [2:0] blockTwelve
);

    wire [2:0] blockOne_next;
    wire [2:0] blockTwo_next;
    wire [2:0] blockThree_next;
    wire [2:0] blockFour_next;
    wire [2:0] blockFive_next;
    wire [2:0] blockSix_next;
    wire [2:0] blockSeven_next;
    wire [2:0] blockEight_next;
    wire [2:0] blockNine_next;
    wire [2:0] blockTen_next;
    wire [2:0] blockEleven_next;
    wire [2:0] blockTwelve_next;

    // Instantiate BRecodeBlock modules
    BRecodeBlock BRecodeBlockOne({inp[1:0], 1'b0}, blockOne_next);
    BRecodeBlock BRecodeBlockTwo(inp[3:1], blockTwo_next);
    BRecodeBlock BRecodeBlockThree(inp[5:3], blockThree_next);
    BRecodeBlock BRecodeBlockFour(inp[7:5], blockFour_next);
    BRecodeBlock BRecodeBlockFive(inp[9:7], blockFive_next);
    BRecodeBlock BRecodeBlockSix(inp[11:9], blockSix_next);
    BRecodeBlock BRecodeBlockSeven(inp[13:11], blockSeven_next);
    BRecodeBlock BRecodeBlockEight(inp[15:13], blockEight_next);
    BRecodeBlock BRecodeBlockNine(inp[17:15], blockNine_next);
    BRecodeBlock BRecodeBlockTen(inp[19:17], blockTen_next);
    BRecodeBlock BRecodeBlockEleven(inp[21:19], blockEleven_next);
    BRecodeBlock BRecodeBlockTwelve(inp[23:21], blockTwelve_next);

    // Sequential logic to register the outputs
    always @(posedge clk) begin
        blockOne <= blockOne_next;
        blockTwo <= blockTwo_next;
        blockThree <= blockThree_next;
        blockFour <= blockFour_next;
        blockFive <= blockFive_next;
        blockSix <= blockSix_next;
        blockSeven <= blockSeven_next;
        blockEight <= blockEight_next;
        blockNine <= blockNine_next;
        blockTen <= blockTen_next;
        blockEleven <= blockEleven_next;
        blockTwelve <= blockTwelve_next;
    end

endmodule
